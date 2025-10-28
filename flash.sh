#!/bin/sh

# write program
# openFPGALoader -b tangnano20k impl/pnr/riscv.fs

# write flash
openFPGALoader -b tangnano20k -f impl/pnr/riscv.fs

