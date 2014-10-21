class ferm::rsync {
    @ferm::rule { "dsa-rsync":
        description     => "Allow rsync access",
        rule            => "&SERVICE(tcp, 873)"
    }
}

