class Cowponder < Formula
  include Language::Python::Virtualenv

  desc "Simple terminal command to display random philosophical thoughts from a cow"
  homepage "https://github.com/maxcai314/homebrew-cowponder"
  url "https://max.xz.ax/cowponder/cowponder-homebrew-v0.0.3.tar.gz"
  sha256 "f9ba2818473e0b74d311a809a1c884ecedfeddfe3b62bf7dc898539a3d4e4ab5"

  # requests resource
  resource "requests" do
    url "https://files.pythonhosted.org/packages/9d/be/10918a2eac4ae9f02f6cfe6414b7a155ccd8f7f9d4380d62fd5b955065c3/requests-2.31.0.tar.gz"
    sha256 "942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1"
  end

  version "0.0.3"

  depends_on "cowsay"
  depends_on "python@3"

  def install
    virtualenv_install_with_resources
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
