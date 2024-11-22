require_relative "./common"

class CcwpLibraryCli < Thor
  desc "count SHOOTNUM", "Counts Images in a shoot"
  option :bytes
  def count(shootnum)
    puts "In count"
  end

end