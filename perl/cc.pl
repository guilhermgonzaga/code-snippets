#!/usr/bin/env perl
# Extract the first line of the file given and run it as a shell command.
# The line must have one of the following formats.
# // cc: <command>
# /* cc: <command> */

use strict;
use warnings;

# Regex patterns for single and multiline comments
my $pattern_single = '^\s*\/\/\s*cc\s*:\s*(.+)(?<!\s)\s*$';
my $pattern_multi  = '^\s*\/\*\s*cc\s*:\s*((?:(?!\*\/).)+)(?<!\s)';

$ARGV[0] // die "Usage: perl cc.pl <file>\n";

# Read file and obtain compile command
open(my $cfile, '<', "$ARGV[0]") // die "Failed to open $ARGV[0]\n";
my $ccmd = get_ccmd($cfile) // die "Command not found in $ARGV[0]\n";
close($cfile);

print "$ccmd\n";
system($ccmd);

sub get_ccmd {
	my ($cfile) = @_;  # Get parameter

	while (my $line = <$cfile>) {
		# If line matches either pattern, return captured command
		if ($line =~ /(?:$pattern_single|$pattern_multi)/) {
			return $1 // $2;
		}
	}

	return undef;
}
