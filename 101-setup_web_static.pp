# This manifest sets up web servers for deployment of web_static

package { 'nginx':
    ensure => installed,
}

service { 'nginx':
    ensure => running,
    enable => true,
}

file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    content => '<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>\n',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
}

file { '/data/web_static/shared':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
}

file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test/',
    owner  => 'ubuntu',
    group  => 'ubuntu',
}

file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "
        server {
            listen 80;
            listen [::]:80;

            server_name taurai.tech;

            location /hbnb_static/ {
                alias /data/web_static/current/;
            }
        }
    ",
    require => Package['nginx'],
}

service { 'nginx':
    ensure => restarted,
}
