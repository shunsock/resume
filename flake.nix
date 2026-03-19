{
  description = "Bun Development Shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        dev-server = pkgs.writeShellApplication {
          name = "dev-server";
          runtimeInputs = [ pkgs.bun ];
          text = ''
            [ -d "node_modules" ] && rm -rf -- "node_modules"
            bun install
            bun run docs:dev
          '';
        };

        build-site = pkgs.writeShellApplication {
          name = "build-site";
          runtimeInputs = [ pkgs.bun ];
          text = ''
            [ -d "node_modules" ] && rm -rf -- "node_modules"
            bun install
            bun run docs:build
          '';
        };
      in {
        apps = {
          default = {
            type = "app";
            program = "${dev-server}/bin/dev-server";
          };
          build = {
            type = "app";
            program = "${build-site}/bin/build-site";
          };
        };

        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.go-task
            pkgs.bun
          ];
          shellHook = ''
            echo "bun version: $(bun --version)"
            echo "go-task version: $(task --version)"
          '';
        };
      });
}
