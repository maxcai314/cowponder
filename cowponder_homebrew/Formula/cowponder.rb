class Cowponder < Formula
  include Language::Python::Virtualenv

  desc "Simple terminal command to display random philosophical thoughts from a cow"
  homepage "https://max.xz.ax/cowponder/"
  url "https://max.xz.ax/cowponder/cowponder-homebrew-v0.0.4.tar.gz"
  sha256 "ef20e3c9ee6e61db8fa0e82d0626fa0383995d6e13c45a4cef0c8e922a2be513"

  depends_on "cowsay"
  depends_on "python-setuptools"
  depends_on "python@3"

  # requests resource
  resource "requests" do
    url "https://files.pythonhosted.org/packages/9d/be/10918a2eac4ae9f02f6cfe6414b7a155ccd8f7f9d4380d62fd5b955065c3/requests-2.31.0.tar.gz"
    sha256 "942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1"
  end

  def install
    virtualenv_install_with_resources
    bin.install "ponder.py" => ponder
    bin.install "cowponder" => cowponder
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
