require_relative "./common"

class CcwpLibraryCli < Thor
  desc "list", "Lists Shoots"
  def list(dir = ".")
    # Look for Directories like sNxx/sNNx/sNNN-GG-Words
    Dir.glob("#{dir}/s???/s???/s???-??-*").each do |shootdir|
      matched = shootdir.match(/s\dxx\/s\d\dx\/s(\d\d\d)-(\w\w)-(.*)/)
      if matched
        (dummy, shootnum, genre, shootname) = *matched
        puts "#{shootnum},#{genre},#{shootname}"
      end
    end
  end
end