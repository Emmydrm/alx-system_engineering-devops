# (Puppet file to configure open file limits on the Holberton user)
exec {'sed_hard':
  path    => '/bin',
  command => 'sed -i "s/holberton hard nofile 5/#holberton hard nofile 5/g" /etc/security/limits.conf',
}

exec {'sed_soft':
  path    => '/bin',
  command => 'sed -i "s/holberton soft nofile 4/#holberton soft nofile 4/g" /etc/security/limits.conf',
}
