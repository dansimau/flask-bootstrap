class sass {
  package { 'sass':
    ensure   => installed,
    provider => gem,
  }
}