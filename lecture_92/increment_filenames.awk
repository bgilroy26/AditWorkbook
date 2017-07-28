#!/usr/bin/awk -F

BEGIN {
    regex = "[2]"
    print "mkdir new"
}
{
    if (match($8,regex)) {
        before = substr($8,1,RSTART-1);
        pattern = substr($8,RSTART,RLENGTH);
        newnumber = pattern + 1
        after = substr($8,RSTART+RLENGTH);
        printf("mv %s new/%s%.2d%s\n", $8, before, newnumber, after);
    }
}
