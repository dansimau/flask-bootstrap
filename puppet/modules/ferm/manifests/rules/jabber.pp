class ferm::jabber {
    @ferm::rule { "jabber":
        description     => "Allow jabber access",
        rule            => "&SERVICE(tcp, (5222 5223 5269 5280))"
    }
}

