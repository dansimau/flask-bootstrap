class ferm::imaps {
    @ferm::rule { "imaps":
        description     => "Allow imaps access",
        rule            => "&SERVICE( tcp, imaps)"
    }
}

