{
  description = "App with NodeJS";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { nixpkgs, ... }:
    let
      supportedSystems = [ "aarch64-darwin" "x86_64-linux" ];
      forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system:
        f {
          pkgs = import nixpkgs {
            inherit system;
          };
        });
    in {
      devShells = forAllSystems ({ pkgs }: {
        default = pkgs.mkShell {
          buildInputs = [ pkgs.nodejs_20 ];
        };
      });
    };
}