#!/usr/bin/python
# coding=UTF-8

import math
import re

from  testmodule.styleformat import heading

'''Write a Regular Expression that will match a date that follows
the following standard YYYY-MM-DD'''

'''The special characters are:

'.'
    (Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified,
     this matches any character including a newline.
'^'
    (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
'$'
    Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also
    matches before a newline. foo matches both ‘foo’ and ‘foobar’, while the regular expression foo$ matches only ‘foo’.
    More interestingly, searching for foo.$ in 'foo1\nfoo2\n' matches ‘foo2’ normally, but ‘foo1’ in MULTILINE mode;
    searching for a single $ in 'foo\n' will find two (empty) matches: one just before the newline, and one at the
    end of the string.
'*'
    Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible.
    ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
'+'
    Causes the resulting RE to match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any
    non-zero number of ‘b’s; it will not match just ‘a’.
'?'
    Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.
*?, +?, ??
    The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour
    isn’t desired; if the RE <.*> is matched against <a> b <c>,
    it will match the entire string, and not just <a>. Adding ? after the qualifier makes it perform the match in
    non-greedy or minimal fashion; as few characters as possible
    will be matched. Using the RE <.*?> will match only <a>.
{m}
    Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to
    match. For example, a{6} will match exactly six 'a' characters,     but not five.
{m,n}
    Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many
    repetitions as possible. For example, a{3,5} will match from 3 to 5 'a' characters. Omitting m specifies a lower
    bound of zero, and omitting n specifies an infinite upper bound. As an example, a{4,}b will match aaaab or a
    thousand 'a' characters followed by a b, but not aaab. The comma may not be omitted or the modifier would be
    confused with the previously described form.
{m,n}?
    Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions
    as possible. This is the non-greedy version of the previous qualifier. For example, on the 6-character string
    'aaaaaa', a{3,5} will match 5 'a' characters, while a{3,5}? will only match 3 characters.
'\'

    Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a
    special sequence; special sequences are discussed below.

    If you’re not using a raw string to express the pattern, remember that Python also uses the backslash as an escape
    sequence in string literals;
    if the escape sequence isn’t recognized by Python’s parser, the backslash and subsequent character are included in
    the resulting string.
    However, if Python would recognize the resulting sequence, the backslash should be repeated twice. This is
    complicated and hard to understand,
    so it’s highly recommended that you use raw strings for all but the simplest expressions.
[]

    Used to indicate a set of characters. In a set:

        Characters can be listed individually, e.g. [amk] will match 'a', 'm', or 'k'.
        Ranges of characters can be indicated by giving two characters and separating them by a '-', for example [a-z]
        will match any lowercase ASCII letter,
        [0-5][0-9] will match all the two-digits numbers from 00 to 59, and [0-9A-Fa-f] will match any hexadecimal
        digit. If - is escaped (e.g. [a\-z])
        or if it’s placed as the first or last character (e.g. [a-]), it will match a literal '-'.
        Special characters lose their special meaning inside sets. For example, [(+*)] will match any of the literal
        characters '(', '+', '*', or ')'.
        Character classes such as \w or \S (defined below) are also accepted inside a set, although the characters they
        match depends on whether LOCALE or UNICODE mode is in force.
        Characters that are not within a range can be matched by complementing the set. If the first character of the
        set is '^', all the characters that are not in the set will be matched.
        For example, [^5] will match any character except '5', and [^^] will match any character except '^'. ^ has no
        special meaning if it’s not the first character in the set.
        To match a literal ']' inside a set, precede it with a backslash, or place it at the beginning of the set. For
        example, both [()[\]{}] and []()[{}] will both match a parenthesis.

'|'
    A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B. An arbitrary
    number of REs can be separated by the '|' in this way.
    This can be used inside groups (see below) as well. As the target string is scanned, REs separated by '|' are tried
    from left to right.
    When one pattern completely matches, that branch is accepted. This means that once A matches, B will not be tested
    further, even if it would produce a longer overall match.
    In other words, the '|' operator is never greedy. To match a literal '|', use \|, or enclose it inside a character
    class, as in [|].
(...)
    Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; the
    contents of a group can be retrieved after a match has been performed,
    and can be matched later in the string with the \number special sequence, described below. To match the literals
    '(' or ')', use \( or \), or enclose them inside a character class: [(] [)].
(?...)
    This is an extension notation (a '?' following a '(' is not meaningful otherwise). The first character after the
    '?' determines what the meaning and further syntax of the construct is.
    Extensions usually do not create a new group; (?P<name>...) is the only exception to this rule. Following are the
    currently supported extensions.
(?iLmsux)

    (One or more letters from the set 'i', 'L', 'm', 's', 'u', 'x'.) The group matches the empty string; the letters
    set the corresponding flags: re.I (ignore case), re.L (locale dependent), re.M (multi-line), re.S (dot matches all),
    re.U (Unicode dependent), and re.X (verbose), for the entire regular expression. (The flags are described in Module
    Contents.) This is useful if you wish to include the flags as part of the regular expression, instead of passing a
    flag argument to the re.compile() function.

    Note that the (?x) flag changes how the expression is parsed. It should be used first in the expression string, or
    after one or more whitespace characters. If there are non-whitespace characters before the flag, the results are
    undefined.
(?:...)
    A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but
    the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.
(?P<name>...)

    Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name
    name. Group names must be valid Python identifiers, and each group name must be defined only once within a regular
    expression. A symbolic group is also a numbered group, just as if the group were not named.

    Named groups can be referenced in three contexts. If the pattern is (?P<quote>['"]).*?(?P=quote) (i.e. matching a
    string quoted with either single or double quotes):
    '''
#Write a Regular Expression that will match an email address.
pat = re.compile(r"(\b([a-zA-Z]{1,25}[0-9a-zA-Z._-]{1,25}\@[a-z.-_]{1,25}\.[a-z]{2,3})\b)")
def reEmail(str):
    mat = re.search(pat, str)
    if mat:
        return mat.group()
    else:
        return "None"

if __name__ == "__main__":
    heading("Module 4 Assignment: 1")
    #mat = re.search(r"\d\d\d\d-([0-2][0-9]|[3][0-1])-([0|1][0-2])", "My date of birth is 1983-00-00")
    mat = re.search(r"\d\d\d\d-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])", "My date of birth is 1983-01-31")


    heading("Module 4 Assignment: 2")
    #Write a Regular Expression that will match a traditional SSN
    '''
    A Social Security Number (SSN) consists of nine digits, commonly written as three fields separated by hyphens:
    AAA-GG-SSSS. The first three-digit field is called the "area number". The central, two-digit field is called the
    "group number". The final, four-digit field is called the "serial number". Area numbers of "000" have never been issued.
    Group codes of "00" aren't assigned Serial number "0000" is never used.
    '''

    mat = re.search(r"(\d\d[1-9]|[1-9]\d\d)-(\d[1-9]|[1-9]\d)-(\d\d\d[1-9]|[1-9]\d\d\d)", "My SSN is 001-03-3544")
    print mat

    heading("Module 4 Assignment: 3")
    #Write a Regular Expression that will match an IPv4 address.[0.0.0.0-255.255.255.255]
    #^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$
    # 55.225.0.255
    mat = re.search(r"(\b([01][0-9][0-9]|[2][0-5][0-5]|\d\d|[0-9])\.){3}([012][0-9][0-5]|\d\d|[0-9])\b",
                    "My IP is 192.168.1.1")
    if mat:
        print mat.group()

    heading("Module 4 Assignment: 4")

    mat = reEmail("My email is mail.kalinga@gmail.com")
    #if mat:
    #    print mat.group()
    #   print mat.groups()

    str = "|          89.6|"
    m = re.findall(r"[0-9.]+", str)[0]
    if len(m):
        print  m
    else:
        print "None"

    str = "|          45|"
    m = re.findall(r"[0-9.]+", str)[0]
    if len(m):
        print  m
    else:
        print "None"

    b = 20
    print "kalinga" if (b > 10) else "sonali"

    heading("Module 4 Assignment: 5")
    # Below is the program to calculate the area of a box. Check how it
    # is working. Correct the program (if required).
    class Box:
        def area(self):
            return self.width * self.height
        def __init__(self, width, height):
            self.width = width
            self.height = height

    # Create an instance of Box.
    x = Box(10, 2)
    # Print area.
    print "Area of the Box: ", x.area()

    heading("Module 4 Assignment: 6")
    # Write a program to calculate distance so that it takes two Points
    #(x1, y1) and (x2, y2) as arguments and displays the calculated
    #distance, using Class.

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def distance(self, point):
            if not (isinstance(point, Point)):
                return -1
            else:
                dist = math.sqrt((self.x - point.x)**2 + (self.y - point.y)** 2)
                return dist

    p1 = Point(12, 0)
    p2 = Point(17, 0)
    print "Distance between p1(12, 0) and p2(17, 0) is: ", p1.distance(p2)
    p1 = Point(3, 0)
    p2 = Point(0, 4)
    print "Distance between p1(3, 0) and p2(0, 4) is: ", p1.distance(p2)

    heading("Module 4 Assignment: 7")
    '''Correct the below program so that output should appear like
    this. [Expected output: x-value: 5 y-value: 7]'''

    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __str__(self):
            return "[x-value: " + str(self.x) + " y-value: %s]"%str(self.y)

        def __add__(self,other):
            self.x = self.x+other.x
            self.y = self.y+other.y
            return self

    p1 = Point(3,4)
    p2 = Point(2,3)
   # print (p1+p2)