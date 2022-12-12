#!/usr/bin/perl

use warnings;
use strict;


our $CONCAT = '.';
our $ADD = '+'; our $MIN = '-'; our $PROD = '*'; our $RDIV = '/';
our $GT = '>'; our $EQ = '==';
our $NEG = 'not'; my $AND = 'and'; our $OR = 'or';
our $LPAR = '('; our $RPAR = ')'; our $ENDINST = ';';
our $ASIG = '='; 
our $tokens = {
	# String
	$CONCAT => 'CONCAT',

	# Arithmetic	
	$ADD  => 'ADD' , $MIN  => 'MIN' , $PROD => 'PROD', $RDIV => 'RDIV',
	
	# Relationals
	$GT   => 'GT'  , $EQ   => 'EQ',
	
	# Conditionals
	$NEG  => 'NEG' , $AND  => 'AND' , $OR   => 'OR',
	
	# Delimiters
	$LPAR => 'LPAR', $RPAR => 'RPAR', $ENDINST => 'EOL',

	# Asign
	$ASIG => 'ASIG'
};

my $INTEGER = qr/^\s*(\d+)\s*$/;
my $FLOAT = qr/^\s*((\d+)?\.(\d+))\s*$/;
my $NUMBER = qr/^\s*($FLOAT|$INTEGER)\s*$/;
my $STRING = qr/^\s*[\"\'].*\[\"\']s*$/;
my $ARITHMETICOP = qr/^\s*(.+)\s+($PROD|$RDIV|$ADD|$MIN)\s+(.+)\s*$/;
my $RELATIONALOP = qr/^\s*(.+)\s+($GT|$EQ)\s+(.+)\s*$/;
my $CONDITIONALOP = qr/^\s*(.+)\s+($AND|$OR)\s+(.+)\s*$/; # bug when there are nested operators, can be fixed tokenizing the parentesis first
my $BOOLEAN = qr/($RELATIONALOP|$CONDITIONALOP|$INTEGER|$STRING)^$/;
our $data_types = {
	number => {
		pattern => $NUMBER,
		specific_type => {
			integer => {
				pattern => $INTEGER,
				translate => 'Int'
			},
			float  =>{
				pattern => $FLOAT,
				translate => 'Float'
			}
		}
	},
	string => {
		pattern => $STRING,
		translate => 'String'
	}
};

our $VARIABLENAME = qr/^\s*(\&[\_a-zA-Z0-9]{255})\s*$/;
our $VARIABLESCOPE = qr/^\s*(let)\s*$/;

sub parser #( $line )
{
	my $line = shift;

	my $order = 0;
	my $ast;
	my $value;
	my $level = 0;
	for my $element ( split( /[ ]+/, $line ) )
	{
		for my $tag ( split ( //, $element ) )
		{
			if ( exists $tokens->{ $tag } )
			{
				if ( defined $value and $value =~ $data_types->{ number }->{ pattern } )
				{
					$ast .= "\t" x $level;
					$ast .= "$order - $value - ";
					if ( $value =~ $data_types->{ number }->{ specific_type }->{ integer }->{ pattern } ) 
					{
						$ast .= $data_types->{ number }->{ specific_type }->{ integer }->{ translate };
					}
					else
					{
						$ast .= $data_types->{ number }->{ specific_type }->{ float }->{ translate };
					}
					$ast .= "\n";
					$order++;
				}

				$level-- if $tag eq $RPAR;
				$ast .= "\t" x $level;
				$level++ if $tag eq $LPAR;
				$ast .= "$order - $tag - $tokens->{ $tag }\n";	
				$order++;
				undef $value;
				next;
			}
			$value .= $tag;
		}
		if ( defined $value and $value =~ $data_types->{ number }->{ pattern } )
		{
			$ast .= "$order - $value - ";
			if ( $value =~ $data_types->{ number }->{ specific_type }->{ integer }->{ pattern } ) 
			{
				$ast .= $data_types->{ number }->{ specific_type }->{ integer }->{ translate };
			}
			else
			{
				$ast .= $data_types->{ number }->{ specific_type }->{ float }->{ translate };
			}
			$ast .= "\n";
			$order++;
			undef $value;
		}
	}

	print "$ast\n";
}

my $test = "54 + -3.2 *(15.2/98)";
print $test, "\n";

&parser( $test );

$test = "\'Prueba\'";
