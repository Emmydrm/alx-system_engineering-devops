# (Puppet file for configuring nginx so that it can handle 3000 requests)
exec {'sed':
  command => 'sed -i "s/worker_processes 4;/worker_processes 3000;/g" /etc/nginx/nginx.conf',
  path    => '/bin',
}

service {'nginx':
  ensure    => 'running',
  subscribe => Exec['sed'],
}
