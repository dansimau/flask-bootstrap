class ferm::www {
    @ferm::rule { "www":
        description     => "Allow www access",
        rule            => "&SERVICE(tcp, (http https))"
    }
}

