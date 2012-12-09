package Netdisco::Daemon::Actions::Port;

use Netdisco::Util::Connect ':all';
use Netdisco::Util::Permissions ':all';
use Netdisco::Daemon::Actions::Util ':all';

use namespace::clean;
use Moo::Role;

sub set_portname {
  my ($self, $job) = @_;
  return _set_port_generic($job, 'alias', 'name');
}

sub set_portcontrol {
  my ($self, $job) = @_;

  my $port = get_port($job->device, $job->port)
    or return error(sprintf "Unknown port name [%s] on device [%s]",
      $job->port, $job->device);

  my $reconfig_check = port_reconfig_check($port);
  return error("Cannot alter port: $reconfig_check")
    if length $reconfig_check;

  return _set_port_generic($job, 'up_admin');
}

sub set_vlan {
  my ($self, $job) = @_;

  my $port = get_port($job->device, $job->port)
    or return error(sprintf "Unknown port name [%s] on device [%s]",
      $job->port, $job->device);

  my $port_reconfig_check = port_reconfig_check($port);
  return error("Cannot alter port: $port_reconfig_check")
    if length $port_reconfig_check;

  my $vlan_reconfig_check = vlan_reconfig_check($port);
  return error("Cannot alter vlan: $vlan_reconfig_check")
    if length $vlan_reconfig_check;

  return _set_port_generic($job, 'vlan');
}

sub _set_port_generic {
  my ($job, $slot, $column) = @_;
  $column ||= $slot;

  my $ip = $job->device;
  my $pn = $job->port;
  (my $data = $job->subaction) =~ s/-\w+//;

  my $port = get_port($ip, $pn)
    or return error("Unknown port name [$pn] on device [$ip]");

  # snmp connect using rw community
  my $info = snmp_connect($ip)
    or return error("Failed to connect to device [$ip] to control port");

  my $iid = get_iid($info, $port)
    or return error("Failed to get port ID for [$pn] from [$ip]");

  my $method = 'set_i_'. $slot;
  my $rv = $info->$method($data, $iid);

  if (!defined $rv) {
      return error(sprintf 'Failed to set [%s] %s to [%s] on [%s]: %s',
                    $pn, $slot, $data, $ip, ($info->error || ''));
  }

  # confirm the set happened
  $info->clear_cache;
  my $check_method = 'i_'. $slot;
  my $state = ($info->$check_method($iid) || '');
  if (ref {} ne ref $state or $state->{$iid} ne $data) {
      return error("Verify of [$pn] $slot failed on [$ip]");
  }

  # update netdisco DB
  $port->update({$column => $data});

  return done("Updated [$pn] $slot status on [$ip] to [$data]");
}

1;