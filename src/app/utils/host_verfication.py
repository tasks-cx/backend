import dns.resolver
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class AuthorizeHost:
    def verfiyHost(domain):
        try:
            result = dns.resolver.resolve(domain, 'TXT')
            answer_raw = result.chaining_result.answer.to_text()
            logging.info('Domain is exist with TXT record {}'.format(answer_raw))
            return True
        except Exception as e:
            logging.error("Domain nont verified with {}".format(e))
            return False 

    def verfiySingature(domain, prjDomin):
        try:
            result = dns.resolver.resolve(domain, 'TXT')
            answer_raw = result.chaining_result.answer.to_text()
            domainValue = answer_raw.split('=')
            if prjDomin == domainValue[1][:len(domainValue[1])-1] and prjDomin != "":
                logging.info("Singature verfied")
                return True
            else:
                logging.info("Singature not verified")
                return False
        except Exception as e:
            logging.error("Domain nont verified with {}".format(e))
            return False