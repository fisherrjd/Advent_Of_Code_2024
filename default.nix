{ pkgs ? import
    (fetchTarball {
      name = "jpetrucciani-2025-02-04";
      url = "https://github.com/jpetrucciani/nix/archive/a60f6cf8780c0e3b96ca75a64d0d5f311dea0a77.tar.gz";
      sha256 = "1pv7njav4yr9fnlrs13vrmlj0nyylhvlfdxvqp8ad72ya9l2ibrp";
    })
    { }
}:
let
  name = "AOC2024";


  tools = with pkgs; {
    cli = [
      jfmt
      nixup
    ];
    python = [
      ruff
      uv
    ];
    scripts = pkgs.lib.attrsets.attrValues scripts;
  };

  scripts = with pkgs; { };
  paths = pkgs.lib.flatten [ (builtins.attrValues tools) ];
  env = pkgs.buildEnv {
    inherit name paths; buildInputs = paths;
  };
in
(env.overrideAttrs (_: {
  inherit name;
  NIXUP = "0.0.8";
})) // { inherit scripts; }
