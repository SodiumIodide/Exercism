use strict;
use warnings;

package Leap;
our $VERSION = "1.0";
use Exporter qw(import);
our @EXPORT_OK = qw(is_leap);

sub is_leap {
    my $year = shift @_;
    if ($year % 4 == 0) {
        if ($year % 100 == 0) {
            if ($year % 400 == 0) {
                return 1;
            }
            return 0;
        }
        return 1;
    }
    return 0;
}

1;
