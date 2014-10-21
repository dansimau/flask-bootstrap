class ferm::dns {
    @ferm::rule { "dns":
        description     => "Allow dns access",
        rule            => "&SERVICE( (tcp udp), domain)"
    }
}

