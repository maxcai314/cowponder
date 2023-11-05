class Cowponder < Formula
  desc "Simple terminal command to display random philosophical thoughts from a cow"
  homepage "https://github.com/maxcai314/homebrew-cowponder"
  url "https://max.xz.ax/cowponder/cowponder-homebrew-v0.0.2.tar.gz"
  sha256 "e58195629860660d095cbe3f56387ff1b6d14ef4b8281d4f622b9c75660d4ff5"

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
