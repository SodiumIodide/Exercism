use warnings;
use strict;
package ETL;
our $VERSION = '1.0';
use Exporter qw(import);
our @EXPORT_OK = qw(transform);

sub transform {
    my $old = shift @_;
    my $new;
    while (my ($key, $values) = each %$old) {
        foreach my $val (@$values) {
            $new->{lc $val} = $key;
        }
    }
    return $new;
}

1;
