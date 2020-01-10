DESTDIR=
CC=gcc
CFLAGS=-O2 -Wall -W -pipe -D_GNU_SOURCE
MANDIR=/usr/share/man/man8
SBINDIR=/sbin

all:		mingetty

install:	all
		install -m 0755 mingetty $(DESTDIR)$(SBINDIR)
		install -m 0644 mingetty.8 $(DESTDIR)$(MANDIR)

mingetty:	mingetty.o

clean:
		rm -f *.o mingetty

