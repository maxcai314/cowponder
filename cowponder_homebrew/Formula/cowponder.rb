class Cowponder < Formula
  desc "Simple terminal command to display random philosophical thoughts from a cow"
  homepage "https://github.com/maxcai314/homebrew-cowponder"
  url "https://xz.ax/cowponder-homebrew-v0.0.2.tar.gz"
  sha256 "9982527b45425239ba0bdce963ec225ea65540185e970ced03fbf27cda350e47"

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
