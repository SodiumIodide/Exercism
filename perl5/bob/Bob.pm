#!usr/bin/env perl

use 5.006;
use strict;
use warnings;

package Bob;

our $VERSION = '1.000';

use Exporter 5.57 qw(import);

our @EXPORT_OK = qw(hey);

sub hey {
    my $input = shift(@_);
    if ($input =~ m/\s+$/ || $input eq '') {
        return "Fine. Be that way!";
    } elsif ($input eq uc $input && $input =~ m/\p{Lu}+/) {
        return "Whoa, chill out!";
    } elsif ($input =~ m/^.+\?$/) {
        return "Sure.";
    } else {
        return "Whatever.";
    }
}

sub main {
    print "What do we say to Bob?\n>>> ";
    my $input = <STDIN>;
    chomp $input;
    print hey($input);
}

main() unless caller;

1;
