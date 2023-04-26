# (Puppet file that executes the pkill command)
exec {'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
