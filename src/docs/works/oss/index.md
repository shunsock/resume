---
title: Open Source Software
description: List of my open source software.
prev:
  text: "Works"
  link: "/works"
next:
  text: "Findy Inc."
  link: "/works/findy"
---

# Open Source Software

## Timezone Translator

Simple command-line utility that converts a given time from one timezone to another. It is written in Rust and you can install via `cargo install tzt`.

### Repository

- [GitHub](https://github.com/shunsock/timezone_translator)
- [Crates.io](https://crates.io/crates/tzt)

### Usage

```sh
$ tzt --time '2024-11-03 01:30:00' --from 'America/New_York' --to 'UTC'
2024-11-03 05:30:00 UTC
```

## dotfiles

My Configuration Files for Development Environment. Updator written by Go is included.

### Repository

- [GitHub](https://github.com/shunsock/dotfiles)

## Shot

⚠️ Under Construction
Shot is a AST-based programming language written in Rust. It is designed to force programmer to write everything what you want to do.

```
let hello: fn = (name: string): void {
    print("Hello, " + name + "!");
    return none;
};

hello("Shunsock");
```

### Repository

- [GitHub](https://github.com/shunsock/shot)

