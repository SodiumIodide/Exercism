use warnings;
use strict;
use bigint;

package Grains;
our $VERSION = '1.0';
use Exporter qw(import);
our @EXPORT_OK = qw(square total);

sub square {
    my $square = shift @_;
    return 2**($square - 1)
}

sub total {
    return 2**64 - 1;
}

1;
