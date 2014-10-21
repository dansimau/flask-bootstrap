class ferm::git {
    @ferm::rule { "git":
        description     => "Allow git access",
        rule            => "&SERVICE(tcp, 9418)"
    }
}

