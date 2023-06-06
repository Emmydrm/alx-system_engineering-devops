# (This puppet file corrects the extension of the class-wp-locale file)
exec {'mv':
  command => 'mv class-wp-locale.php class-wp-locale.phpp',
  cwd     => '/var/www/html/wp-includes',
  path    => '/bin',
}
