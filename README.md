# expert_system
Abstract: The goal of this project is to make a propositional calculus expert system.

The goal of this project is to make a propositional calculus expert system.

https://en.wikipedia.org/wiki/Expert_system

* The following symbols are defined, in order of decreasing priority:
  * • ( and ) which are fairly obvious. Example : A + (B | C) => D
  * • ! which means NOT. Example : !B
  * • + which means AND. Example : A + B
  * • | which means OR. Example : A | B
  * • ˆ which means XOR. Example : A ˆ B
  * • => which means "implies". Example : A + B => C
  * • <=> which means "if and only if". Example : A + B <=> C

III.2 Input file format
>zaz@blackjack:~/expert/$ cat -e example_input.txt
> '# this is a comment$
> '# all the required rules and symbols, along with the bonus ones, will be
> '# shown here. spacing is not important
>C => E # C implies E
>A + B + C => D # A and B and C implies D
>A | B => C # A or B implies C
>A + !B => F # A and not B implies F
>C | !G => H # C or not G implies H
>V ^ W => X # V xor W implies X
>A + B => Y + Z # A and B implies Y and Z
>C | D => X | V # C or D implies X or V
>E + F => !V # E and F implies not V
>A + B <=> C # A and B if and only if C
>A + B <=> !C # A and B if and only if not C
>=ABG # Initial facts : A, B and G are true. All others are false.
># If no facts are initially true, then a simple "=" followed
># by a newline is used
>?GVX # Queries : What are G, V and X ?
>zaz@blackjack:~/expert/$
