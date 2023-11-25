# Hedron Stenotype

This plugin for Plover provides a layout with additional keys and remapped keys to support Hedron Theory and further extensibility.

In addition to split S, the number bar and asterisk are split, and two additional keys are added on the far left to make the layout symmetric. The right bank keys are renamed to accommodate the changes in the theory. The number bar keys are treated as ordinary keys and do not act as special number keys, so the names of the other keys do not change.

Full steno order with this plugin is `#%@^+STKPWHR~AOEU*LRPSTKGZYD`. At this time `%@~` are unused by Hedron Theory and can be assigned as needed for custom use.

Expected keymap as follows:

```
 ####   %%%% 
@+TPH~ *LPTGY
^SKWR~ *RSKZD
    AO EU    
```

The default Gemini PR keymap in this plugin assigns `#B` for `@` and `#C` for `^`. To enable the use of the far left keys on an EcoSteno, the firmware must be modified accordingly and reflashed.

Currently structured as a single module `hedron_stenotype` but as the scope expands it may become necessary to switch to a package structure.
