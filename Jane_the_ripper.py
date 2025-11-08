import hashlib 

def main():
    """
    Controls the flow of the program, gathering user input and calling
    the main cracking logic.
    """
    print("--- Python Dictionary Password Cracker ---")

   
    hash_file_path = input("Enter path to hash file (e.g., hashes.txt): ")
    wordlist_path = input("Enter path to wordlist file (e.g., wordlist.txt): ")

   
    crack_passwords(hash_file_path, wordlist_path)

def crack_passwords(hash_file_path, wordlist_path):
    """
    Performs the dictionary attack by comparing wordlist hashes against
    a set of target hashes.
    """
    target_hashes = set() 
    print("\n--- LOADING TARGET HASHES ---")

    try:
        
        with open(hash_file_path, 'r') as f:
            for line in f:
                
                clean_hash = line.strip()
                if clean_hash: 
                    target_hashes.add(clean_hash)
                    print(f"[+] Loaded {len(target_hashes)} unique hashes successfully.")
        
    except FileNotFoundError:
        print(f"ERROR: Hash file not found at '{hash_file_path}'")
        return 
    uncracked_hashes = set(target_hashes) 
    cracked_count = 0
    
    print("\n--- CRACKING STARTED ---")
    
    try:
       
        with open(wordlist_path, 'r', encoding='latin-1') as f: 
            for word in f:
                
                clean_word = word.strip()
                encoded_word = clean_word.encode('utf-8')
                hash_object = hashlib.md5(encoded_word)
                word_hash = hash_object.hexdigest()
                if word_hash in uncracked_hashes:
                    
                    print(f"[+] Cracked: {word_hash}  -->  {clean_word}")
                    

                    uncracked_hashes.remove(word_hash)
                    cracked_count += 1
                    if not uncracked_hashes:
                        break
    except FileNotFoundError:
        print(f"ERROR: Wordlist file not found at '{wordlist_path}'")
        return
    print("\n--- CRACKING FINISHED ---")
    
    if uncracked_hashes:
        print(f"[-] FAILED to crack {len(uncracked_hashes)} hash(es) out of {len(target_hashes)} total.")
        print("Uncracked Hashes:")
        for failed_hash in uncracked_hashes:
            print(f"[-] FAILED: {failed_hash}")
    else:
        print(f"[!] All {cracked_count} hashes cracked successfully!")

    print(f"[!] Total cracked: {cracked_count}")
    
if __name__ == "__main__":
    main()