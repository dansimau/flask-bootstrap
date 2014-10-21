class ferm::ftp {
    @ferm::rule { "dsa-ftp":
        description     => "Allow ftp access",
        rule            => "&SERVICE(tcp, 21)"
    }
}
