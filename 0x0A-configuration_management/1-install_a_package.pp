##!/usr/bin/pup
# Install flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
#install werkzweg
package { 'werkzweg':
  ensure   => '2.2.2',
  provider => 'pip3'
}
