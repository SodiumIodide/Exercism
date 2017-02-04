use warnings;
use strict;

package Raindrops;
our $VERSION = '1.0';
use Exporter qw(import);
our @EXPORT_OK = qw(convert);

sub convert {
    my $number = shift @_;
    my $outp = '';
    local *divisible = sub {$number % shift @_ == 0};
    if (divisible(3)) {$outp = $outp.'Pling';}
    if (divisible(5)) {$outp = $outp.'Plang';}
    if (divisible(7)) {$outp = $outp.'Plong';}
    return $outp || $number;
}

1;
