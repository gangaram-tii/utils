{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [ 
    pkgs.gcc
    pkgs.python311Full
    pkgs.python311Packages.virtualenv
  ];  

  shellHook = ''
    if [ ! -d .venv ]; then
      virtualenv .venv
      source .venv/bin/activate
      pip install requests beautifulsoup4
    else
      source .venv/bin/activate
      pip install requests beautifulsoup4
    fi
    echo "Welcome to your Python development environment."
  '';
}

