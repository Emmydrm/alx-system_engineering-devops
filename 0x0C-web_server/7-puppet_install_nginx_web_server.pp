# (Puppet manifest to configure a brand new webserver)
package {'nginx':
  ensure => 'installed',
}
file {'/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
}
file {'/usr/share/nginx/html/custom_404':
  ensure  => 'present',
  path    => '/usr/share/nginx/html/custom_404',
  content => 'Ceci n\'est pas une page',
}
exec {'command':
  path    => '/bin',
  command => 'sed -i "48i\	location \/redirect_me {\n		try_files \$uri =301;\n	}" /etc/nginx/sites-available/default',
}
service {'nginx':
  ensure => 'running',
  enable => true,
}
