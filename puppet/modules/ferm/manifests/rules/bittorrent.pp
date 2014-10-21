class ferm::bittorrent {
    @ferm::rule { "bittorrent":
        description     => "Allow smtp access",
        rule            => "&SERVICE( ( tcp udp), 51413 )"
    }
    @ferm::rule { "bttrack":
        description     => "Allow bttrack access",
        rule            => "&SERVICE( tcp, 6969 )"
    }
}

