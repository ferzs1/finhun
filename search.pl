#! /usr/bin/perl
use CGI;
use DBI;
use CGI::Session;
use strict;
use warnings;

my $cgi = CGI->new();
my $session  = CGI::Session->new($cgi) or die CGI->Session->errstr;
my $username = $cgi->param('username') // '';
my $searchword = $cgi->param('search');


my $driver = "mysql";
my $database = "sunkari_dict";
my $dsn = "DBI:$driver:database=$database";
my $userid = "sunkarisql";
my $password = "sqlJQ3Qd0";

my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;

my $sth = $dbh->prepare("SELECT word
                        FROM Entry
						WHERE status = 'done' AND word = '$searchword'");
$sth->execute() or die $DBI::errstr;
my $word;
while (my @row = $sth->fetchrow_array()) {
   ($word) = @row;
}

print $cgi->redirect('../index2.cgi');

$sth->finish();
