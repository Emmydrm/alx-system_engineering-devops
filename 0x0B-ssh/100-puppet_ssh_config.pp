# (This puppet file works on file)
file {'/etc/ssh/ssh_config':
  path    => '/etc/ssh/ssh_config',
  content => 'PasswordAuthentication no
	      IdentityFile ~/.ssh/school',
}
