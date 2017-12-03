# RefactoringDevTools

Example:
script_refactorer.py "static Set<String> propertyIds = new HashSet<>\(\);\s*static {\s*(?:propertyIds\.add\([A-Za-z_0-9]*\);\s*)*}" "new HashSet<>\(\);\s*static {"="Sets.newHashSet(" "propertyIds\.add\("="" "\);"="," ",\s*}"=");" /home/king/Work/git/ambari/ambari-server/src/main/java

script_refactorer.py "static Map<Resource.Type, String> keyPropertyIds = new HashMap<>\(\);\s*static {\s*(?:keyPropertyIds\.put\([ \.\,A-Za-z_0-9]*\);\s*)*}" "new HashMap<>\(\);\s*static {"="ImmutableMap.<Resource.Type, String> builder()" "keyPropertyIds\.put"=".put" "\);"=")" "}"=".build();" /home/king/Work/git/ambari/ambari-server/src/main/java