use warnings;
use strict;
package Hamming;
our $VERSION = '1.0';
use Exporter qw(import);
our @EXPORT_OK = qw(compute);

sub compute {
    my ($orig, $comp) = @_;
    if (length($orig) != length($comp)) {
        die "DNA strands must be of equal length";
    }
    my $count = ($orig ^ $comp) =~ tr/\0//c;
    return $count;
}

1;
