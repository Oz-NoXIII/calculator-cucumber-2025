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

          shellHook = ''
            echo "🔧 Installing Node.js dependencies..."
            cd src/web
            if [ -f package-lock.json ] || [ -f package.json ]; then
              npm install
            fi

            echo "🚀 Starting dev server..."
            npm run dev
          '';
        };
      });
    };
}