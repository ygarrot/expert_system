# expert_system
Abstract: The goal of this project is to make a propositional calculus expert system.

The goal of this project is to make a propositional calculus expert system.

https://en.wikipedia.org/wiki/Expert_system

* The following symbols are defined, in order of decreasing priority:
  *  ( and ) which are fairly obvious. Example : A + (B | C) => D
  *  ! which means NOT. Example : !B
  *  + which means AND. Example : A + B
  *  | which means OR. Example : A | B
  *  ˆ which means XOR. Example : A ˆ B
  *  => which means "implies". Example : A + B => C
  *  <=> which means "if and only if". Example : A + B <=> C

III.2 Input file format
>zaz@blackjack:~/expert/$ cat -e example_input.txt<br />
> '# this is a comment$<br />
> '# all the required rules and symbols, along with the bonus ones, will be<br />
> '# shown here. spacing is not important<br />
>C => E # C implies E
>A + B + C => D # A and B and C implies D<br />
>A | B => C # A or B implies C<br />
>A + !B => F # A and not B implies F<br />
>C | !G => H # C or not G implies H<br />
>V ^ W => X # V xor W implies X<br />
>A + B => Y + Z # A and B implies Y and Z<br />
>C | D => X | V # C or D implies X or V<br />
>E + F => !V # E and F implies not V<br />
>A + B <=> C # A and B if and only if C<br />
>A + B <=> !C # A and B if and only if not C<br />
>=ABG # Initial facts : A, B and G are true. All others are false.<br />
> # If no facts are initially true, then a simple "=" followed<br />
> # by a newline is used<br />
> ?GVX # Queries : What are G, V and X ?<br />
