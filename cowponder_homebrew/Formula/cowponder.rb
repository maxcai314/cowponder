class Cowponder < Formula
  desc "Simple terminal command to display random philosophical thoughts from a cow"
  homepage "https://github.com/maxcai314/homebrew-cowponder"
  url "https://max.xz.ax/cowponder/cowponder-homebrew-v0.0.3.tar.gz"
  sha256 "f9ba2818473e0b74d311a809a1c884ecedfeddfe3b62bf7dc898539a3d4e4ab5"

  version "0.0.3"

  depends_on "cowsay"
  depends_on "python@3"

  def install
    bin.install "ponder"
    bin.install "cowponder"
    etc.install "cowthoughts.txt"
  end

  def uninstall
    rm bin/"ponder"
    rm bin/"cowponder"
    rm etc/"cowthoughts.txt"
  end

  test do
    assert_predicate bin/"ponder", :exist?
    assert_predicate bin/"cowponder", :exist?
    assert_predicate etc/"cowthoughts.txt", :exist?
  end
end
