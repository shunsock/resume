{
  description = "Bun Development Shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.go-task
            pkgs.bun
          ];
          shellHook = ''
            echo "bun version: $(bun --version)"
            echo "go-task version: $(task --version)"
            bun install
          '';
        };
      });
}
