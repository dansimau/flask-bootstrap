class ferm::smtp {
    @ferm::rule { "smtp":
        description     => "Allow smtp access",
        rule            => "&SERVICE(tcp, smtp)"
    }
}

