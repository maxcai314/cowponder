class Cowponder < Formula
  desc "Simple terminal command to display random philosophical thoughts from a cow"
  homepage "https://github.com/maxcai314/homebrew-cowponder"
  url "https://max.xz.ax/cowponder/cowponder-homebrew-v0.0.2.tar.gz"
  sha256 "1dcbb47be7c9d0fcc589e7744e31901fe85d9014784d7a32069b1d5f4cf1847d"
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
